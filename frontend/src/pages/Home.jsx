import { motion } from "framer-motion";
import { Link } from "react-router-dom";

export default function Home() {
  return (
    <div className="relative min-h-screen overflow-hidden flex flex-col justify-center items-center text-center px-6 bg-black text-white">

      {/* 🔥 Animated Background Glow */}
      <div className="absolute inset-0 -z-10">
        <div className="absolute w-[600px] h-[600px] bg-purple-600 opacity-20 blur-3xl rounded-full top-[-200px] left-[-200px] animate-pulse"></div>
        <div className="absolute w-[600px] h-[600px] bg-blue-600 opacity-20 blur-3xl rounded-full bottom-[-200px] right-[-200px] animate-pulse"></div>
      </div>

      {/* 🔥 Headline */}
      <motion.h1
        initial={{ opacity: 0, y: -60 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 1 }}
        className="text-6xl md:text-7xl font-extrabold mb-6 leading-tight"
      >
        <span className="bg-gradient-to-r from-blue-400 via-purple-400 to-pink-500 bg-clip-text text-transparent animate-gradient-x">
          FinSight AI
        </span>
        <br />
        Financial Intelligence Engine
      </motion.h1>

      {/* 🔥 Subtitle */}
      <motion.p
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.6 }}
        className="text-gray-400 max-w-3xl text-lg mb-12"
      >
        Transform complex financial statements into actionable strategic insights using a specialized sovereign AI model.
      </motion.p>

      {/* 🔥 CTA Buttons */}
      <motion.div
        initial={{ opacity: 0, y: 40 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 1 }}
        className="flex flex-col md:flex-row gap-8"
      >
        <Link to="/pdf">
          <motion.button
            whileHover={{ scale: 1.08 }}
            whileTap={{ scale: 0.95 }}
            className="px-10 py-5 text-lg font-semibold bg-gradient-to-r from-blue-500 to-purple-600 rounded-2xl shadow-[0_0_40px_rgba(139,92,246,0.5)] hover:shadow-[0_0_60px_rgba(139,92,246,0.9)] transition"
          >
            🚀 Analyze Financial PDF
          </motion.button>
        </Link>

        <Link to="/manual">
          <motion.button
            whileHover={{ scale: 1.08 }}
            whileTap={{ scale: 0.95 }}
            className="px-10 py-5 text-lg font-semibold border border-purple-500 rounded-2xl backdrop-blur-md bg-white/5 hover:bg-purple-500/20 transition shadow-lg"
          >
            ✍️ Enter Data Manually
          </motion.button>
        </Link>
      </motion.div>

      {/* 🔥 Floating Stats Section */}
      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 1.5 }}
        className="grid grid-cols-1 md:grid-cols-3 gap-8 mt-20 max-w-5xl w-full"
      >
        {[
          { title: "AI Ratio Interpretation", desc: "Specialized SLM trained for financial diagnostics." },
          { title: "Managerial Insights", desc: "Strategic classification and risk alerts." },
          { title: "Instant Analysis", desc: "Upload PDF or enter data in seconds." }
        ].map((item, i) => (
          <motion.div
            key={i}
            whileHover={{ scale: 1.05 }}
            className="bg-white/5 backdrop-blur-lg p-8 rounded-2xl border border-white/10 shadow-xl"
          >
            <h3 className="text-xl font-semibold text-blue-400 mb-3">
              {item.title}
            </h3>
            <p className="text-gray-400">
              {item.desc}
            </p>
          </motion.div>
        ))}
      </motion.div>

    </div>
  );
}
