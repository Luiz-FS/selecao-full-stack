import React, { Suspense } from 'react';
import { Outlet } from "react-router-dom";
import { LinearProgress } from '@mui/material';
import Box from '@mui/material/Box';
import CssBaseline from '@mui/material/CssBaseline';
import Toolbar from '@mui/material/Toolbar';
import NavBar from './navbar';

const Root = props => {
    return (
        <Box sx={{ display: 'flex', backgroundColor: "rgba(236, 246, 255, 0.3);" , minHeight: "100vh"}}>
            <CssBaseline />
            <NavBar></NavBar>
            <Box component="main" sx={{ flexGrow: 1, p: 3, padding: 0 , maxWidth: "100vw"}}>
                <Toolbar />
                <Suspense fallback={<LinearProgress />}>
                    <Outlet />
                </Suspense>
            </Box>
        </Box>
    )
}



export default Root;