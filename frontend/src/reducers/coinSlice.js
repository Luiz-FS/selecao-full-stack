import { createAsyncThunk, createSlice } from '@reduxjs/toolkit';
import { getCoins } from '../services/coinService';

const initialState = {
    coins: []
}

export const loadCoins = createAsyncThunk(
    'coins/load',
    async () => {
        return getCoins();
    }
);


export const coinSlice = createSlice({
    name: 'coin',
    initialState,
    extraReducers: (builder) => {
        builder
        .addCase(loadCoins.fulfilled, (state, action) => {
            state.coins = action.payload;
        })
        .addCase(loadCoins.rejected, (state) => {
            alert("Falha ao carregar moedas");
        });
    }
});


export const selectCoins = (state) => state.coin.coins;

export default coinSlice.reducer;