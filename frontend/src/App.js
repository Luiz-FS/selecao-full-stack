import React from 'react';
import { createBrowserRouter, Navigate, RouterProvider } from "react-router-dom";
import Root from "./layouts";
import Login from "./views/login";
import Home from "./views/home";


const router = createBrowserRouter([
  {
    path: "/",
    element: <Root />,
    children: [
      {
        index: true,
        element: <Navigate to="/home" replace={true}/>
      },
      {
        path: "login",
        element: <Login />
      },
      {
        path: "home",
        element: <Home/>
      }
    ]
  }
])


function App() {
  return (
    <RouterProvider router={router}>
    </RouterProvider>
  );
}

export default App;
