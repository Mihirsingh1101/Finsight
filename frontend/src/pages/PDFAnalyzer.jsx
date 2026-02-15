import { useState } from "react";
import axios from "axios";
import ResultCard from "../components/ResultCard";
import { motion } from "framer-motion";

export default function PDFAnalyzer() {

  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleSubmit = async () => {

    if (!file) {
      setError("Please upload a PDF file.");
      return;
    }

    setError("");
    setLoading(true);
    setResult(null);

    try {
      const formData = new FormData();
      formData.append("file", file);

      const res = await axios.post(
        "http://localhost:8000/analyze_pdf",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data"
          }
        }
      );

      setResult(res.data);
    } catch (err) {
      setError("Error analyzing PDF. Please try again.");
    }

    setLoading(false);
  };

  return (
    <div className="min-h-screen p-10">

      <motion.div
        initial={{ opacity: 0, y: -30 }}
        animate={{ opacity: 1, y: 0 }}
        className="bg-white/5 backdrop-blur-lg p-8 rounded-2xl border border-white/10 shadow-xl max-w-3xl mx-auto"
      >

        <h2 className="text-2xl font-semibold text-blue-400 mb-6">
          Upload Financial Statement (PDF)
        </h2>

        <div className="flex flex-col gap-6">

          <input
            type="file"
            accept="application/pdf"
            onChange={(e)=>setFile(e.target.files[0])}
            className="bg-gray-800 p-3 rounded-lg"
          />

          <button
            onClick={handleSubmit}
            className="bg-gradient-to-r from-blue-500 to-purple-600 px-6 py-3 rounded-xl shadow-lg hover:scale-105 transition"
          >
            Analyze Financial Data
          </button>

          {error && (
            <div className="text-red-400">
              {error}
            </div>
          )}

        </div>
      </motion.div>

      {/* 🔥 Loader */}
      {loading && (
        <div className="flex justify-center mt-12">
          <div className="animate-spin h-14 w-14 border-4 border-blue-400 border-t-transparent rounded-full"></div>
        </div>
      )}

      {/* 🔥 Result */}
      {result && !loading && (
        <ResultCard data={result} />
      )}

    </div>
  );
}
