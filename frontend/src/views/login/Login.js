import { Box, Button, Container, Hidden, OutlinedInput, Typography } from "@mui/material";
import React, {useState} from "react";
import { Navigate } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import { login, selectIsLoggedIn } from '../../reducers/loginSlice';
import "./Login.css";
import { Page } from "../../components";

const Login = () => {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const loggedIn = useSelector(selectIsLoggedIn);
    const dispatch = useDispatch();

    const handleLogin = (e) => {
        e.preventDefault();
        dispatch(login({email, password}));

        return false
    }

    return (
        <Page title="Realtimequotation: Login">
            <Container maxWidth="false" className="login-container">
                {loggedIn && <Navigate to="/home" replace={true} />}
                <Hidden mdDown>
                    <img src="/beeteller.png" style={{maxWidth: "50%"}}></img>
                </Hidden>
                <div className="login-form-box">
                    <Box sx={{display: "flex", flexDirection: "column", alignItems: "center", maxWidth: "60%"}}>
                        <Typography variant="h4" component="h4" sx={{color: "black", textAlign: "center"}}>
                            Olá! Bem vindo de volta.
                        </Typography>
                        <Typography variant="h5" component="h5" sx={{color: "#828282", textAlign: "center"}}>
                            Faça login com seus dados inseridos durante o seu registro.
                        </Typography>
                        <Box component="form" autoComplete="off" sx={{width: "100%"}} onSubmit={handleLogin}>
                            <div className="login-input-box">
                                <p>Email</p>
                                <OutlinedInput type="email" value={email} onChange={(e) => {setEmail(e.target.value)}} name="email" className="login-input" placeholder="exemplo@email.com" required />
                            </div>
                            <div className="login-input-box">
                                <p>Senha</p>
                                <OutlinedInput name="password" type="password" value={password} onChange={(e) => {setPassword(e.target.value)}} className="login-input" placeholder="Enter password" required/>
                            </div>
                            <Button type="submit" className="login-form-btn-submit" variant="contained">Login</Button>
                        </Box>
                    </Box>
                </div>
            </Container>
        </Page>
    )
}

export default Login