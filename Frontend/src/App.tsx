import { useState } from "react";
import { Guide } from "./Pages/Guide";
import { Retourner } from "./Pages/Retourner";

const App = () => {
  const [page, setPage] = useState(1);

  return (
    <div className="h-screen w-screen flex flex-col text-green-50 overflow-x-auto">
      <div className="w-full h-32 min-h-32 flex flex-row items-center justify-evenly bg-stone-500 font-semibold border-b-2 border-green-500">
        <div
          className="text-[40px] text-white w-full h-full hover:bg-green-300 hover:text-stone-500 flex justify-center items-center"
          onClick={() => setPage(0)}
        >
          Guide
        </div>
        <div
          className="text-[40px] text-white w-full h-full hover:bg-green-300 hover:text-stone-500 flex justify-center items-center"
          onClick={() => setPage(1)}
        >
          Le challenge
        </div>
      </div>
      <div className=" my-[2rem] flex-grow text-green-100 flex justify-center p-[3rem] md:px-[15rem] text-[30px]">
        {/* {page === 0 && <Accueil />} */}
        {page === 0 && <Guide />}
        {page === 1 && <Retourner />}
      </div>
    </div>
  );
};

export default App;
