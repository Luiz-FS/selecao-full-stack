import { configureStore } from '@reduxjs/toolkit';
import { loginReducer, coinReducer, quotationReducer } from '../reducers';

export const store = configureStore({
  reducer: {
    user: loginReducer,
    coin: coinReducer,
    quotation: quotationReducer,
  },
});
