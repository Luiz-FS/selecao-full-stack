import { createAsyncThunk, createSlice } from '@reduxjs/toolkit';
import { getQuotations } from '../services/quotationService';

const initialState = {
    quotations: [],
    page: 1,
    count: 0,
    rowsPerPage: 10
}

export const loadQuotations = createAsyncThunk(
    'quotations/load',
    async (coinId, thunkApi) => {
        const state = thunkApi.getState();
        const page = selectPage(state);
        const rowsPerPage = selectRowsPerPage(state);

        return getQuotations(coinId, page, rowsPerPage);
    }
);

export const quotationSlice = createSlice({
    name: 'quotation',
    initialState,
    reducers: {
        setPage: (state, action) => {
            state.page = action.payload;
        },
        setRowsPerPage: (state, action) => {
            state.rowsPerPage = action.payload;
        }
    },
    extraReducers: (builder) => {
        builder
        .addCase(loadQuotations.fulfilled, (state, action) => {
            state.count = action.payload["count"];
            state.quotations = action.payload["results"];
        })
        .addCase(loadQuotations.rejected, (state) => {
            alert("Falha ao carregar cotações");
        });
    }
});

export const {setPage, setRowsPerPage} = quotationSlice.actions;

export const selectQuotations = (state) => state.quotation.quotations;
export const selectPage = (state) => state.quotation.page;
export const selectRowsPerPage = (state) => state.quotation.rowsPerPage;
export const selectCount = (state) => state.quotation.count;

export default quotationSlice.reducer;