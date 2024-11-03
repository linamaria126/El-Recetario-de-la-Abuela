import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
//importamos las páginas
import { Home } from "./pages/Home";
import { Register } from "./pages/Register";
import  { Navbar }   from "./components/Navbar";
import { Ingredients} from  "./pages/Ingredients";
import { Recipies } from "./pages/Recipies";


function App() {
  return (
    <BrowserRouter>
      <Navbar />
      <Routes>
        <Route path="/" element={<Navigate to="/home" />} />
        <Route path="/home" element={<Home />} />
        <Route path="/register" element={<Register />} />
        <Route path="/ingredients" element={<Ingredients />} />
        <Route path="/recipies" element={<Recipies />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
