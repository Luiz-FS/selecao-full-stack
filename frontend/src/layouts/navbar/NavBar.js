import * as React from 'react';
import AppBar from '@mui/material/AppBar';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import './NavBar.css'

const NavBar = () => {
    return (
        <AppBar position="fixed" className='nav-app-bar'>
            <Toolbar className='nav-toolbar nav-toolbar-reponsive'>
                <div className='nav-logo'>
                    <Typography variant="h6" noWrap component="div" sx={{color: "black"}}>
                        beeteller 
                    </Typography>
                    <div className='nav-logo-divider'></div>
                    <Typography variant="h6" noWrap component="div" sx={{fontSize: "1rem", color: "#BDBDBD"}}>
                        COTAÇÕES <svg style={{marginLeft: "10px"}} width="14" height="21" viewBox="0 0 14 21" fill="none" xmlns="http://www.w3.org/2000/svg">
                                    <path d="M13 10.5L10 19.5L4 1.5L1 10.5" stroke="#BDBDBD" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                                </svg>

                    </Typography>
                </div>
                <Typography variant="h6" noWrap component="div" sx={{color: "black"}}>
                    EN
                </Typography>
            </Toolbar>
        </AppBar>
    );
}


export default NavBar