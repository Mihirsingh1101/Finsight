import { motion } from "framer-motion";

export default function ResultCard({ data }) {

  // Optional: dynamic health score (example logic)
  const healthScore = 75; // You can calculate dynamically later

  return (
    <motion.div
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      className="mt-12 space-y-8"
    >

      {/* 🔥 Financial Health Score Section */}
      <motion.div
        whileHover={{ scale: 1.02 }}
        className="bg-white/5 backdrop-blur-lg p-6 rounded-2xl border border-white/10 shadow-xl"
      >
        <div className="text-sm text-gray-400 mb-2">
          Financial Health Score
        </div>

        <div className="w-full bg-gray-800 rounded-full h-4">
          <div
            className="bg-gradient-to-r from-green-400 to-blue-500 h-4 rounded-full transition-all duration-700"
            style={{ width: `${healthScore}%` }}
          ></div>
        </div>

        <div className="text-right mt-2 text-blue-400 font-semibold">
          {healthScore}%
        </div>
      </motion.div>

      {/* 🔥 Category Insights */}
      {Object.entries(data.slm_interpretation).map(([category, text]) => (
        <motion.div
          key={category}
          whileHover={{ scale: 1.02 }}
          className="bg-white/5 backdrop-blur-lg p-6 rounded-2xl border border-white/10 shadow-xl"
        >
          <h2 className="text-xl font-semibold text-blue-400 mb-4 capitalize">
            {category}
          </h2>

          <p className="text-gray-300 whitespace-pre-line">
            {text}
          </p>
        </motion.div>
      ))}

    </motion.div>
  );
}
