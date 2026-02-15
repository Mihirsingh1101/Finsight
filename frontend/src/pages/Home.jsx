import { motion } from "framer-motion";
import { Link } from "react-router-dom";
import Navbar from "../components/Navbar";

export default function Home() {

  return (

<>
<Navbar />


<div className="relative min-h-screen flex flex-col justify-center items-center text-center px-6 text-white overflow-hidden">


{/* ✅ MAIN GRADIENT BACKGROUND */}

<div className="absolute inset-0 -z-20 bg-gradient-to-br from-black via-blue-950 to-black"></div>


{/* ✅ BIG VISIBLE GRADIENT BLOBS */}

<div className="absolute top-[-150px] left-[-150px] w-[600px] h-[600px] bg-blue-500 rounded-full blur-[150px] opacity-40 -z-10"></div>


<div className="absolute bottom-[-150px] right-[-150px] w-[600px] h-[600px] bg-purple-500 rounded-full blur-[150px] opacity-40 -z-10"></div>


<div className="absolute top-[40%] left-[30%] w-[500px] h-[500px] bg-cyan-400 rounded-full blur-[150px] opacity-30 -z-10"></div>



{/* HERO TITLE */}

<motion.h1
initial={{ opacity: 0, y: -40 }}
animate={{ opacity: 1, y: 0 }}
transition={{ duration: 1 }}
className="text-6xl md:text-7xl font-extrabold mb-6 leading-tight"
>

<span className="bg-gradient-to-r from-cyan-400 via-blue-400 to-purple-500 bg-clip-text text-transparent">

FinSight AI

</span>

<br/>

Financial Intelligence Engine

</motion.h1>



{/* SUBTITLE */}

<motion.p
initial={{ opacity: 0 }}
animate={{ opacity: 1 }}
transition={{ delay: 0.5 }}
className="text-gray-300 max-w-2xl text-lg mb-12"
>

Transform financial statements into intelligent insights using sovereign AI.

</motion.p>



{/* BUTTONS */}

<motion.div
initial={{ opacity: 0, y: 40 }}
animate={{ opacity: 1, y: 0 }}
transition={{ delay: 1 }}
className="flex flex-col md:flex-row gap-6"
>


<Link to="/pdf">

<motion.button
whileHover={{ scale: 1.05 }}
className="px-10 py-5 text-lg font-semibold bg-gradient-to-r from-cyan-500 to-blue-600 rounded-2xl shadow-lg"
>

Analyze Financial PDF

</motion.button>

</Link>



<Link to="/manual">

<motion.button
whileHover={{ scale: 1.05 }}
className="px-10 py-5 text-lg font-semibold border border-cyan-400 rounded-2xl bg-white/5"
>

Enter Data Manually

</motion.button>

</Link>


</motion.div>



</div>

</>

  );

}
