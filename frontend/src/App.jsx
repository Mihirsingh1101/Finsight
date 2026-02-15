import { BrowserRouter, Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";
import Home from "./pages/Home";
import PDFAnalyzer from "./pages/PDFAnalyzer";
import ManualAnalyzer from "./pages/ManualAnalyzer";

function App() {
  return (
    <BrowserRouter>
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/pdf" element={<PDFAnalyzer />} />
        <Route path="/manual" element={<ManualAnalyzer />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
