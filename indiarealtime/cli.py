"""
Command-line interface for IndiaRealTime
"""

import click
from tabulate import tabulate
from .client import IndiaRealTime


@click.group()
@click.version_option(version="0.1.0")
def cli():
    """IndiaRealTime CLI - Live India data at your fingertips"""
    pass


@cli.command()
@click.option('--commodity', help='Commodity name (wheat, rice, onion, etc.)')
@click.option('--state', help='State name')
@click.option('--city', help='Market/city name')
@click.option('--limit', default=10, help='Number of results')
def mandi(commodity, state, city, limit):
    """Get mandi prices for agricultural commodities"""
    irt = IndiaRealTime()
    prices = irt.mandi_prices(
        commodity=commodity,
        state=state,
        city=city,
        limit=limit,
    )
    
    if not prices:
        click.echo("No results found", err=True)
        return
    
    table_data = [
        [
            p.commodity,
            p.market,
            p.state,
            p.city,
            f"₹{p.price:.0f}",
            p.unit,
        ]
        for p in prices
    ]
    
    click.echo(tabulate(
        table_data,
        headers=["Commodity", "Market", "State", "City", "Price", "Unit"],
        tablefmt="grid"
    ))


@cli.command()
@click.option('--type', 'fuel_type', default='petrol', 
              type=click.Choice(['petrol', 'diesel', 'lpg']),
              help='Fuel type')
@click.option('--state', help='State name')
@click.option('--city', help='City name')
def fuel(fuel_type, state, city):
    """Get current fuel prices"""
    irt = IndiaRealTime()
    prices = irt.fuel_prices(fuel_type=fuel_type, state=state, city=city)
    
    if not prices:
        click.echo(f"No {fuel_type} prices found", err=True)
        return
    
    table_data = [
        [p.state, p.city, f"₹{p.price:.2f}", p.unit, p.updated_at]
        for p in prices
    ]
    
    click.echo(tabulate(
        table_data,
        headers=["State", "City", "Price", "Unit", "Updated"],
        tablefmt="grid"
    ))


@cli.command()
@click.option('--city', help='City name')
@click.option('--state', help='State name')
def aqi(city, state):
    """Get air quality index (AQI) data"""
    irt = IndiaRealTime()
    results = irt.air_quality(city=city, state=state)
    
    if not results:
        click.echo("No AQI data found", err=True)
        return
    
    table_data = [
        [
            r.city,
            r.state,
            r.aqi,
            r.aqi_category,
            f"{r.pm25:.0f}",
            f"{r.pm10:.0f}",
        ]
        for r in results
    ]
    
    click.echo(tabulate(
        table_data,
        headers=["City", "State", "AQI", "Category", "PM2.5", "PM10"],
        tablefmt="grid"
    ))


@cli.command()
@click.option('--state', help='State name')
def weather(state):
    """Get weather alerts"""
    irt = IndiaRealTime()
    alerts = irt.weather_alerts(state=state)
    
    if not alerts:
        click.echo("No weather alerts", err=True)
        return
    
    for alert in alerts:
        click.echo(f"\n[{alert.alert_type}] {alert.state}")
        click.echo(f"  {alert.description}")
        click.echo(f"  Severity: {alert.severity}")
        if alert.issued_at:
            click.echo(f"  Issued: {alert.issued_at}")


@cli.command()
@click.option('--limit', default=5, help='Number of matches to show')
def cricket(limit):
    """Get live cricket scores"""
    irt = IndiaRealTime()
    scores = irt.cricket_scores(limit=limit)
    
    if not scores:
        click.echo("No cricket matches", err=True)
        return
    
    for score in scores:
        status_icon = "🔴" if score.status == "Live" else "○"
        click.echo(f"{status_icon} {score.teams}")
        click.echo(f"   {score.score_team1}", nl=False)
        if score.score_team2:
            click.echo(f"  vs  {score.score_team2}")
        else:
            click.echo()
        click.echo(f"   [{score.format}] {score.status}")
        if score.current_over:
            click.echo(f"   Over: {score.current_over}")
        click.echo()


@cli.command()
@click.option('--base', default='INR', help='Base currency')
@click.option('--symbols', help='Target currencies (comma-separated)')
def currency(base, symbols):
    """Get currency exchange rates"""
    irt = IndiaRealTime()
    symbol_list = symbols.split(',') if symbols else None
    rates = irt.currency_rates(base=base, symbols=symbol_list)
    
    if not rates:
        click.echo("No currency data available", err=True)
        return
    
    table_data = [
        [base, symbol, f"{rate:.4f}"]
        for symbol, rate in rates.items()
    ]
    
    click.echo(tabulate(
        table_data,
        headers=["From", "To", "Rate"],
        tablefmt="grid"
    ))


@cli.command()
def health():
    """Check API health status"""
    irt = IndiaRealTime()
    status = irt.health()
    
    click.echo(f"API Status: {status.get('status', 'unknown')}")
    click.echo(f"Last Updated: {status.get('last_updated', 'N/A')}")
    
    if 'services' in status:
        click.echo("\nService Status:")
        for service, info in status['services'].items():
            status_emoji = "✓" if info.get('status') == 'operational' else "✗"
            click.echo(f"  {status_emoji} {service}: {info.get('status')} ({info.get('uptime', 'N/A')}%)")


def main():
    """Entry point for CLI"""
    cli()


if __name__ == '__main__':
    main()
