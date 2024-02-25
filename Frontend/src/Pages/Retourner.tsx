import { useEffect, useState } from "react";

import pythonWeekend from "./PythonWeekendPage.json";
import React from "react";
// ... (other imports)

const BACK_END_URL = "http://127.0.0.1:5000";

export const Retourner = () => {
  const [name, setName] = useState<string>(
    localStorage.getItem("1337_Name") || ""
  );
  const [submittedName, setSubmittedName] = useState("");
  const [showSubmitCodeButtons, setShowSubmitCodeButtons] = useState<boolean[]>(
    []
  );
  const [points, setPoints] = useState(0);

  const PythonWeekendPage = ({ data }: { data: any }) => {
    return (
      <div className="container mx-auto py-4 px-2 ">
        {data.pythonWeekend.map((item, index) => (
          <div key={index} className="mb-20">
            <h2 className="text-3xl font-semibold mb-4 text-green-300">
              {index + 1} - {item.title}
            </h2>
            <div className="ml-8">
              <p className="text-gray-100 mb-4">{item.description}</p>
              <pre className="bg-gray-600 p-4 rounded-lg whitespace-pre-wrap">
                {item.output}
              </pre>
              {!showSubmitCodeButtons[index] ? (
                <div className="flex flex-row gap-8 items-center">
                  <button
                    className="bg-green-500 text-white p-2 px-6 rounded-lg hover:bg-green-300 hover:text-stone-500 mt-8"
                    onClick={() => {
                      // Handle the logic for submitting code
                      setSubmiteCode(item.title);
                      setLevel(index + 1);
                      console.log("Code submitted!");
                      // focus the textarea `textareaRef`
                      // if (textareaRef.current) textareaRef.current.focus();
                    }}
                  >
                    Submit Code
                  </button>
                  {error === index + 1 && (
                    <p className="text-red-500 font-semibold mt-8">
                      Code submitted failed!
                    </p>
                  )}
                </div>
              ) : (
                // show success message
                <p className="text-green-500 font-semibold mt-8">
                  Code submitted successfully!
                </p>
              )}
            </div>
          </div>
        ))}
      </div>
    );
  };

  const handleSubmit = (e?: React.KeyboardEvent<HTMLInputElement>) => {
    if ((e && e.key === "Enter") || !e) {
      const requestBody = {
        username: submittedName,
      };

      fetch(BACK_END_URL + "/add_user", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(requestBody),
      })
        .then((response) => response.json())
        .then((data) => {
          console.log(data);
        })
        .catch((error) => {
          console.error("Error:", error);
        });

      localStorage.setItem("1337_Name", submittedName);
      setName(submittedName);
    }
  };

  useEffect(() => {
    if (name !== "") {
      // Make a GET request to get the user columns
      fetch(`${BACK_END_URL}/get_user_columns/${name}`)
        .then((response) => {
          if (!response.ok) {
            throw new Error("User not found");
          } else {
            return response.json();
          }
        })
        .then((data) => {
          // Check the columns to determine whether to show the buttons
          setShowSubmitCodeButtons([
            data.bonjour_le_monde,
            data.entree_utilisateur,
            data.calculatrice_de_base,
            data.convertisseur_temperature,
            data.calculateur_surface,
            data.convertisseur_devise,
            data.generateur_mot_de_passe,
            data.obtenir_adresse_ip,
          ]);
          setPoints(data.points);
        })
        .catch((error) => {
          console.error("Error:", error);
          localStorage.removeItem("1337_Name");
          setName("");
        });
    }
  }, [name]);

  const [error, setError] = useState<number>(0);

  const handeleSubmitCode = () => {
    //
    const requestBody = {
      user_name: name,
      level: level,
      code: code,
    };
    fetch(BACK_END_URL + "/test", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(requestBody),
    })
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
        setShowSubmitCodeButtons([
          data.progress.bonjour_le_monde,
          data.progress.entree_utilisateur,
          data.progress.calculatrice_de_base,
          data.progress.convertisseur_temperature,
          data.progress.calculateur_surface,
          data.progress.convertisseur_devise,
          data.progress.generateur_mot_de_passe,
          data.progress.obtenir_adresse_ip,
        ]);
        setPoints(data.points || 0);
      })
      .catch((error) => {
        console.error("Error:", error);
        setError(level);
      });
    setSubmiteCode("");
    // setCode("");
  };

  const [submiteCode, setSubmiteCode] = useState<string>("");
  const [code, setCode] = useState<string>("");
  const [level, setLevel] = useState<number>(0);
  const textareaRef = React.useRef(null);

  return (
    <div className="App">
      <div className={submiteCode === "" ? "hidden" : ""}>
        <h1 className="absolute z-50  top-10 left-10 text-4xl font-bold text-center my-8 text-green-500">
          {submiteCode}
        </h1>
        <textarea
          ref={textareaRef}
          className="absolute z-50 min-w-[65%] min-h-[65%] max-w-[65%] max-h-[65%] mx-auto rounded-lg bg-slate-700 border-2 border-green-500 p-4"
          value={code}
          onChange={(e) => setCode(e.target.value)}
        ></textarea>
        <button
          className=" absolute z-50 bg-green-500 text-white p-2 rounded-lg hover:bg-green-300 hover:text-stone-500 bottom-20 right-28"
          onClick={handeleSubmitCode}
        >
          Submit
        </button>
        <div
          className=" absolute flex justify-center items-center z-10 h-screen w-screen bg-gray-700 left-0 top-0 opacity-90 "
          onClick={() => setSubmiteCode("")}
        ></div>
      </div>

      <header className="App-header"></header>
      <main>
        {name !== "" ? (
          <div>
            <h1 className=" text-end text-blue-400 font-bold">{name}</h1>
            <h1 className="text-4xl font-bold text-center my-8">
              My Python Weekend
              <br />
              <span className="text-green-300 font-normal text-[25px]">
                vous avez{" "}
                <span
                  className={points <= 10 ? `text-red-600` : `text-green-600`}
                >
                  {points}
                </span>{" "}
                / 100 points
              </span>
            </h1>
            <PythonWeekendPage data={pythonWeekend} />
          </div>
        ) : (
          <>
            <h1 className="text-4xl font-bold text-center my-8">
              C'est quoi ton nom?
            </h1>
            <input
              className="text-black p-2"
              type="text"
              value={submittedName}
              onChange={(e) => {
                setSubmittedName(e.target.value);
              }}
              onKeyPress={handleSubmit}
            />
            <button
              className="bg-green-500 text-white p-2 rounded-lg hover:bg-green-300 hover:text-stone-500 ml-3"
              onClick={() => handleSubmit()}
            >
              Submit
            </button>
          </>
        )}
      </main>
    </div>
  );
};
