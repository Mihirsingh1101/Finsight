import { motion } from "framer-motion";
import { Link } from "react-router-dom";
import logo from "../assets/logo.png";

export default function Navbar() {
  return (

<motion.nav
initial={{ y: -80, opacity: 0 }}
animate={{ y: 0, opacity: 1 }}
transition={{ duration: 0.6 }}
className="
fixed top-0 left-0 w-full z-50
bg-white/5 backdrop-blur-xl
border-b border-white/10
shadow-lg shadow-black/20
"
>

<div className="max-w-7xl mx-auto px-6 py-4 flex justify-between items-center">


{/* ✅ Logo + Name */}

<Link to="/" className="flex items-center gap-3">


<img
src={logo}
alt="FinSight AI Logo"
className="w-10 h-10 object-contain"
/>


<h1 className="
text-2xl font-bold
bg-gradient-to-r
from-cyan-400
via-blue-400
to-purple-500
bg-clip-text text-transparent
">

FinSight AI

</h1>


</Link>



{/* Links */}

<div className="flex gap-8 items-center">


<Link to="/">

<motion.button
whileHover={{ scale: 1.05 }}
className="
px-5 py-2
rounded-xl
border border-cyan-400/40
text-cyan-300
bg-cyan-500/10
hover:bg-gradient-to-r
hover:from-cyan-500
hover:to-blue-600
hover:text-white
transition-all duration-300
"
>

Home

</motion.button>

</Link>



<Link to="/pdf">

<motion.button
whileHover={{ scale: 1.05 }}
className="text-gray-300 hover:text-cyan-400 transition"
>

Analyze PDF

</motion.button>

</Link>



<Link to="/manual">

<motion.button
whileHover={{ scale: 1.05 }}
className="text-gray-300 hover:text-cyan-400 transition"
>

Manual Entry

</motion.button>

</Link>


</div>


</div>

</motion.nav>

  );
}
