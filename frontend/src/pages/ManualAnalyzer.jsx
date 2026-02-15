import { useState } from "react";
import axios from "axios";
import ResultCard from "../components/ResultCard";
import { motion } from "framer-motion";

export default function ManualAnalyzer() {

  const [form, setForm] = useState({});
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  // Fields expected by backend
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

  const requiredFields = [
    "current_assets",
    "current_liabilities",
    "total_assets",
    "total_equity",
    "revenue",
    "net_profit",
    "ebit",
    "interest_expense"
  ];

  const handleChange = (e) => {
    setForm({
      ...form,
      [e.target.name]: e.target.value === "" ? "" : parseFloat(e.target.value)
    });
  };

  const handleSubmit = async () => {

    // Validation
    for (let field of requiredFields) {
      if (form[field] === undefined || form[field] === "") {
        setError(`Please enter ${field.replaceAll("_", " ")}`);
        return;
      }
    }

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
      setError("Failed to analyze. Please check backend connection.");
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

        <h2 className="text-3xl font-semibold text-blue-400 mb-10 text-center">
          Enter Financial Data Manually
        </h2>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">

          {fields.map((field) => (
            <div key={field} className="flex flex-col">
              <label className="text-sm text-gray-400 mb-2 capitalize">
                {field.replaceAll("_", " ")}
              </label>
              <input
                type="number"
                step="any"
                name={field}
                value={form[field] ?? ""}
                onChange={handleChange}
                className="bg-gray-800 p-3 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
              />
            </div>
          ))}

        </div>

        <button
          onClick={handleSubmit}
          className="mt-10 w-full bg-gradient-to-r from-blue-500 to-purple-600 px-6 py-4 rounded-xl shadow-lg hover:scale-105 transition text-lg font-semibold"
        >
          Analyze Financial Data
        </button>

        {error && (
          <div className="text-red-400 mt-4 text-center">
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
