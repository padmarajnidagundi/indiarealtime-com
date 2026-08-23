'use client';

import { useState, useEffect } from 'react';

interface MandiPrice {
  commodity: string;
  market: string;
  state: string;
  city: string;
  price: number;
  unit: string;
  updated_at: string;
}

export default function MandiPricesPage() {
  const [prices, setPrices] = useState<MandiPrice[]>([]);
  const [loading, setLoading] = useState(true);
  const [commodity, setCommodity] = useState('wheat');
  const [error, setError] = useState<string | null>(null);

  const fetchPrices = async () => {
    setLoading(true);
    setError(null);
    try {
      const response = await fetch(
        `http://localhost:8000/mandi/prices?commodity=${commodity}&limit=20`
      );
      if (!response.ok) throw new Error(`API error: ${response.status}`);
      const data = await response.json();
      setPrices(data.results);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to fetch prices');
      setPrices([]);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchPrices();
  }, [commodity]);

  return (
    <div className="min-h-screen bg-gradient-to-br from-orange-50 to-amber-50 p-6">
      <div className="max-w-6xl mx-auto">
        {/* Header */}
        <div className="mb-8">
          <h1 className="text-4xl font-bold text-amber-900 mb-2">
            🌾 Mandi Prices
          </h1>
          <p className="text-amber-700">
            Live agricultural commodity prices across India
          </p>
        </div>

        {/* Commodity Selector */}
        <div className="bg-white rounded-lg shadow-md p-6 mb-8">
          <label className="block text-sm font-medium text-gray-700 mb-3">
            Select Commodity
          </label>
          <div className="grid grid-cols-2 md:grid-cols-4 gap-3">
            {['wheat', 'rice', 'onion', 'potato', 'cotton', 'soybean'].map(
              (com) => (
                <button
                  key={com}
                  onClick={() => setCommodity(com)}
                  className={`px-4 py-2 rounded-lg font-medium transition-colors ${
                    commodity === com
                      ? 'bg-orange-500 text-white'
                      : 'bg-gray-200 text-gray-800 hover:bg-gray-300'
                  }`}
                >
                  {com.charAt(0).toUpperCase() + com.slice(1)}
                </button>
              )
            )}
          </div>
        </div>

        {/* Error Message */}
        {error && (
          <div className="bg-red-100 border-l-4 border-red-500 text-red-700 p-4 mb-8">
            <p className="font-bold">Error</p>
            <p>{error}</p>
          </div>
        )}

        {/* Loading State */}
        {loading && (
          <div className="text-center py-12">
            <div className="inline-block animate-spin rounded-full h-12 w-12 border-b-2 border-orange-500"></div>
            <p className="text-gray-600 mt-4">Loading prices...</p>
          </div>
        )}

        {/* Prices Table */}
        {!loading && prices.length > 0 && (
          <div className="overflow-x-auto bg-white rounded-lg shadow-md">
            <table className="w-full">
              <thead className="bg-amber-100">
                <tr>
                  <th className="px-6 py-3 text-left text-sm font-bold text-gray-700">
                    Market
                  </th>
                  <th className="px-6 py-3 text-left text-sm font-bold text-gray-700">
                    State
                  </th>
                  <th className="px-6 py-3 text-left text-sm font-bold text-gray-700">
                    City
                  </th>
                  <th className="px-6 py-3 text-right text-sm font-bold text-gray-700">
                    Price (₹)
                  </th>
                  <th className="px-6 py-3 text-left text-sm font-bold text-gray-700">
                    Updated
                  </th>
                </tr>
              </thead>
              <tbody className="divide-y divide-gray-200">
                {prices.map((price, idx) => (
                  <tr
                    key={idx}
                    className="hover:bg-orange-50 transition-colors"
                  >
                    <td className="px-6 py-4 text-sm font-medium text-gray-900">
                      {price.market}
                    </td>
                    <td className="px-6 py-4 text-sm text-gray-600">
                      {price.state}
                    </td>
                    <td className="px-6 py-4 text-sm text-gray-600">
                      {price.city}
                    </td>
                    <td className="px-6 py-4 text-sm font-bold text-right text-orange-600">
                      ₹{price.price.toFixed(2)}
                    </td>
                    <td className="px-6 py-4 text-xs text-gray-500">
                      {new Date(price.updated_at).toLocaleDateString()}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}

        {!loading && prices.length === 0 && !error && (
          <div className="text-center py-12 bg-white rounded-lg">
            <p className="text-gray-500 text-lg">No prices found</p>
          </div>
        )}
      </div>
    </div>
  );
}
