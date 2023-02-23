import React, {useState, useEffect} from "react";
import { Box, Container, IconButton, MenuItem, Select, Typography } from "@mui/material";
import CachedIcon from '@mui/icons-material/Cached';
import { useDispatch, useSelector } from "react-redux";
import { Navigate } from "react-router-dom";
import {selectIsLoggedIn} from '../../reducers/loginSlice';
import { selectCoins, loadCoins } from '../../reducers/coinSlice'
import { selectCount, selectPage, selectRowsPerPage, selectQuotations, setPage, setRowsPerPage, loadQuotations } from '../../reducers/quotationSlice';
import { CoinCard, QuotationTable } from "../../components"
import './Home.css'
  

const Home = () => {
    const isLoggedIn = useSelector(selectIsLoggedIn);
    const [coinSelect, setCoinSelect] = useState("");
    const [fistLoad, setFirstLoad] = useState(false);
    const [quotationRows, setQuotationRows] = useState([]);
    const coins = useSelector(selectCoins);
    const quotationsCount = useSelector(selectCount);
    const quotationsPage = useSelector(selectPage);
    const quotationsRowsPerPage = useSelector(selectRowsPerPage);
    const quotations = useSelector(selectQuotations);
    const dispatch = useDispatch();

    const handleChange = (event) => {
        setCoinSelect(event.target.value);
        dispatch(loadQuotations(event.target.value));
    };

    const getCoins = () => {
        dispatch(loadCoins());
    }

    const handleSetPage = (page) => {
        dispatch(setPage(page + 1));
        dispatch(loadQuotations(coinSelect));
    }

    const handlesetRowsPerPage = (rowsPerPage) => {
        dispatch(setRowsPerPage(rowsPerPage));
        dispatch(loadQuotations(coinSelect));
    }

    useEffect(() => {
        if (!fistLoad && coins.length > 0) {
            setCoinSelect(coins[0].id);
            setFirstLoad(true);
            dispatch(loadQuotations(coins[0].id));
        }
    }, [coins, fistLoad, dispatch]);

    useEffect(() => {
        if (quotations.length > 0) {
            const coin = coins.find(coin => coin.id === coinSelect ? coin : false);
            setQuotationRows(quotations.map(quotation => {
                return {
                    name: coin.description,
                    ...quotation
                }
            }));
        }
    }, [coins, quotations, coinSelect]);

    useEffect(() => {
        if (isLoggedIn) {    
            getCoins();
        }
    }, []);

    return (
        <Container sx={{display: "flex", flexDirection: "column", rowGap: "50px", paddingTop: "40px"}}>
            {!isLoggedIn && <Navigate to="/login" replace={true}/>}
            <Box sx={{display: "flex", flexDirection: "row", justifyContent: "space-between"}}>
                <Typography variant="h4" component="h4" sx={{color: "black", fontWeight: "bold"}}>
                    Moedas
                </Typography>
                <IconButton aria-label="reload" onClick={() => {getCoins()}}>
                    <CachedIcon/>
                </IconButton>
            </Box>
            <Box className="home-coin-container">
                {coins.map((coin, i) => <CoinCard name={coin.name} price={coin.price} description={coin.description} key={i}></CoinCard>)}
            </Box>
            <Box sx={{display: "flex", flexDirection: "row", justifyContent: "space-between"}}>
                <Typography variant="h4" component="h4" sx={{color: "black", fontWeight: "bold"}}>
                    Cotações
                </Typography>
                <Select
                    value={coinSelect}
                    onChange={handleChange}
                    displayEmpty
                    inputProps={{ 'aria-label': 'Select Coin' }}
                    sx={{width: "200px"}}
                    >
                    {coins.map((coin, i) => {
                           return i === 0
                            ? <MenuItem value={coin.id} key={coin.id} selected={true}>{coin.description}</MenuItem>
                            : <MenuItem value={coin.id} key={coin.id}>{coin.description}</MenuItem>
                        })
                    }
                </Select>
            </Box>
            {quotationRows.length > 0 
                ? <QuotationTable 
                    rows={quotationRows}
                    page={quotationsPage - 1}
                    rowsPerPage={quotationsRowsPerPage}
                    count={quotationsCount}
                    onPageChange={handleSetPage}
                    onRowsPerPageChange={handlesetRowsPerPage}
                    />
                : ""
            }
        </Container>
    )
}

export default Home;