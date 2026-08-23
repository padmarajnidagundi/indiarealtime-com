"""
Google Sheets integration example - Auto-update a sheet with live prices
"""

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.apps import sheets_v4
from indiarealtime import IndiaRealTime
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

class SheetsIntegration:
    def __init__(self, credentials_file='credentials.json', token_file='token.json'):
        self.credentials_file = credentials_file
        self.token_file = token_file
        self.service = None
        self.irt = IndiaRealTime()
        self.authenticate()
    
    def authenticate(self):
        """Authenticate with Google Sheets API"""
        creds = None
        
        # Load existing token
        try:
            creds = Credentials.from_authorized_user_file(self.token_file, SCOPES)
        except FileNotFoundError:
            pass
        
        # Get new token if needed
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    self.credentials_file, SCOPES
                )
                creds = flow.run_local_server(port=0)
            
            # Save token for later
            with open(self.token_file, 'w') as token:
                token.write(creds.to_json())
        
        self.service = sheets_v4.build('sheets', 'v4', credentials=creds)
    
    def update_mandi_prices(self, spreadsheet_id, sheet_name='Mandi Prices'):
        """Update mandi prices sheet"""
        logger.info(f"Fetching mandi prices...")
        prices = self.irt.mandi_prices(limit=100)
        
        # Prepare data
        values = [
            ['Commodity', 'Market', 'State', 'City', 'Price (₹)', 'Unit', 'Updated']
        ]
        
        for price in prices:
            values.append([
                price.commodity,
                price.market,
                price.state,
                price.city,
                price.price,
                price.unit,
                price.updated_at,
            ])
        
        # Update sheet
        body = {'values': values}
        self.service.spreadsheets().values().update(
            spreadsheetId=spreadsheet_id,
            range=f"'{sheet_name}'!A1",
            valueInputOption='RAW',
            body=body
        ).execute()
        
        logger.info(f"Updated {len(prices)} mandi prices in {sheet_name}")
    
    def update_fuel_prices(self, spreadsheet_id, sheet_name='Fuel Prices'):
        """Update fuel prices sheet"""
        logger.info(f"Fetching fuel prices...")
        petrol = self.irt.fuel_prices(fuel_type='petrol', limit=50)
        diesel = self.irt.fuel_prices(fuel_type='diesel', limit=50)
        lpg = self.irt.fuel_prices(fuel_type='lpg', limit=50)
        
        # Prepare data
        values = [
            ['Fuel Type', 'State', 'City', 'Price (₹)', 'Updated']
        ]
        
        for price in petrol + diesel + lpg:
            values.append([
                price.fuel_type.upper(),
                price.state,
                price.city,
                price.price,
                price.updated_at,
            ])
        
        # Update sheet
        body = {'values': values}
        self.service.spreadsheets().values().update(
            spreadsheetId=spreadsheet_id,
            range=f"'{sheet_name}'!A1",
            valueInputOption='RAW',
            body=body
        ).execute()
        
        logger.info(f"Updated {len(petrol + diesel + lpg)} fuel prices in {sheet_name}")
    
    def update_aqi_data(self, spreadsheet_id, sheet_name='Air Quality'):
        """Update air quality sheet"""
        logger.info(f"Fetching AQI data...")
        results = self.irt.air_quality()
        
        # Prepare data
        values = [
            ['City', 'State', 'AQI', 'Category', 'PM2.5', 'PM10', 'Updated']
        ]
        
        for result in results:
            values.append([
                result.city,
                result.state,
                result.aqi,
                result.aqi_category,
                result.pm25,
                result.pm10,
                result.updated_at,
            ])
        
        # Update sheet
        body = {'values': values}
        self.service.spreadsheets().values().update(
            spreadsheetId=spreadsheet_id,
            range=f"'{sheet_name}'!A1",
            valueInputOption='RAW',
            body=body
        ).execute()
        
        logger.info(f"Updated {len(results)} AQI records in {sheet_name}")
    
    def update_all(self, spreadsheet_id):
        """Update all sheets"""
        self.update_mandi_prices(spreadsheet_id)
        self.update_fuel_prices(spreadsheet_id)
        self.update_aqi_data(spreadsheet_id)

if __name__ == '__main__':
    # Usage
    sheets = SheetsIntegration()
    
    # Replace with your spreadsheet ID
    SPREADSHEET_ID = 'your-spreadsheet-id-here'
    
    sheets.update_all(SPREADSHEET_ID)
    logger.info("All sheets updated!")
