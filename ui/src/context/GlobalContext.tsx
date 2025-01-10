import React, { createContext, useState } from "react";

interface IGlobalContext {
  isLogedIn: boolean;
  setIsLogedIn: React.Dispatch<React.SetStateAction<boolean>>
}

export const GlobalContext = createContext({} as IGlobalContext)

export const GlobalContextProvider: React.FC<{
	children: React.ReactNode;
}> = ({ children }) => {
  const [isLogedIn, setIsLogedIn] = useState<boolean>(false);

  return (
    <GlobalContext.Provider
      value={{
        isLogedIn,
        setIsLogedIn
      }}
    >
      {children}
    </GlobalContext.Provider>
  )
}