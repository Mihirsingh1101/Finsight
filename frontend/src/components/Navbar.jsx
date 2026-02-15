import { Link } from "react-router-dom";
import { motion } from "framer-motion";

export default function Navbar() {
  return (
    <motion.div
      initial={{ y: -60 }}
      animate={{ y: 0 }}
      className="backdrop-blur-md bg-white/5 border-b border-white/10 p-5 flex justify-between items-center"
    >
      <h1 className="text-2xl font-bold bg-gradient-to-r from-blue-400 to-purple-500 bg-clip-text text-transparent">
        FinSight AI
      </h1>

      <div className="flex gap-8 text-gray-300">
        <Link to="/" className="hover:text-blue-400 transition">Home</Link>
        <Link to="/pdf" className="hover:text-blue-400 transition">PDF</Link>
        <Link to="/manual" className="hover:text-blue-400 transition">Manual</Link>
      </div>
    </motion.div>
  );
}
