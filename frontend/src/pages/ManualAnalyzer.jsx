import { useState } from "react";
import axios from "axios";
import ResultCard from "../components/ResultCard";
import { motion } from "framer-motion";

export default function ManualAnalyzer() {

  const [form, setForm] = useState({});
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const fields = [
    "current_assets",
    "current_liabilities",
    "inventory",
    "cash",
    "revenue",
    "net_profit",
    "total_assets",
    "total_equity",
    "ebit",
    "interest_expense",
    "receivables",
    "total_debt"
  ];

  const handleChange = (e) => {
    setForm({
      ...form,
      [e.target.name]: parseFloat(e.target.value) || 0
    });
  };

  const handleSubmit = async () => {

    setError("");
    setResult(null);
    setLoading(true);

    try {
      const res = await axios.post(
        "http://localhost:8000/analyze_manual",
        form
      );

      setResult(res.data);
    } catch (err) {
      setError("Failed to analyze. Please check inputs or backend.");
    }

    setLoading(false);
  };

  return (
    <div className="min-h-screen p-10">

      <motion.div
        initial={{ opacity: 0, y: -30 }}
        animate={{ opacity: 1, y: 0 }}
        className="bg-white/5 backdrop-blur-lg p-8 rounded-2xl border border-white/10 shadow-xl max-w-4xl mx-auto"
      >

        <h2 className="text-2xl font-semibold text-blue-400 mb-8">
          Enter Financial Data Manually
        </h2>

        <div className="grid grid-cols-2 gap-6">
          {fields.map((field) => (
            <input
              key={field}
              type="number"
              step="any"
              name={field}
              placeholder={field.replaceAll("_", " ").toUpperCase()}
              onChange={handleChange}
              className="bg-gray-800 p-3 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
          ))}
        </div>

        <button
          onClick={handleSubmit}
          className="mt-8 w-full bg-gradient-to-r from-blue-500 to-purple-600 px-6 py-3 rounded-xl shadow-lg hover:scale-105 transition"
        >
          Analyze Financial Data
        </button>

        {error && (
          <div className="text-red-400 mt-4">
            {error}
          </div>
        )}

      </motion.div>

      {/* Loader */}
      {loading && (
        <div className="flex justify-center mt-12">
          <div className="animate-spin h-14 w-14 border-4 border-blue-400 border-t-transparent rounded-full"></div>
        </div>
      )}

      {/* Result */}
      {result && !loading && (
        <ResultCard data={result} />
      )}

    </div>
  );
}
