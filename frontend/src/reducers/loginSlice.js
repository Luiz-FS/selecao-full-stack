import { createAsyncThunk, createSlice } from '@reduxjs/toolkit';
import { login as loginRequest } from '../services/authService';

const user = JSON.parse(localStorage.getItem("user"));

const initialState = user 
    ? {isLoggedIn: true, user, status: "idle"}
    : {isLoggedIn: false, user: null, status: "idle"};


export const login = createAsyncThunk(
    'login/sendLoginRequest',
    async (credentials) => {
        console.log(credentials);
        const { email, password } = credentials;
        return loginRequest(email, password);
    }
)

export const loginSlice = createSlice({
    name: "login",
    initialState,
    extraReducers: (builder) => {
        builder
        .addCase(login.pending, (state) => {
            state.status = "loading";
        })
        .addCase(login.fulfilled, (state, action) => {
            state.status = "idle";
            state.isLoggedIn = true;
            state.user = action.payload;
        })
        .addCase(login.rejected, (state) => {
            alert("Falha na autenticação");
            state.status = "rejected";
        });
    }
})

export const selectIsLoggedIn = (state) => state.user.isLoggedIn;
export const selectUser = (state) => state.user.user;
export const selectStatus = (state) => state.user.status;

export default loginSlice.reducer;