import React from "react";
import PropTypes from 'prop-types';
import { Paper } from "@mui/material";
import './CoinCard.css'


const CoinCard = props => {
    const {
        name,
        price,
        description
    } = props;

    const formatPrice = (price) =>  Number(price).toLocaleString('pt-br', {
        minimumFractionDigits: 2,
        maximumFractionDigits: 2
    });

    return (
        <Paper elevation={5} className="coin-card-container">
            <div className="coin-card-container-box">
                <div className="coin-description-container">
                    <p className="coin-card-name">{name}</p>
                    <div className="coin-price-box"><span className="coin-card-price-simbol">R$</span> <span className="coin-card-price-value">{formatPrice(price)}</span></div>
                    <p style={{fontSize: "14px", color: "#828282"}}>{description}</p>
                </div>
                <svg width="64" height="64" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <rect width="64" height="64" rx="32" fill="#F4C23B"/>
                    <path d="M32 21V43" stroke="black" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                    <path d="M37 25H29.5C28.5717 25 27.6815 25.3687 27.0251 26.0251C26.3687 26.6815 26 27.5717 26 28.5C26 29.4283 26.3687 30.3185 27.0251 30.9749C27.6815 31.6313 28.5717 32 29.5 32H34.5C35.4283 32 36.3185 32.3687 36.9749 33.0251C37.6313 33.6815 38 34.5717 38 35.5C38 36.4283 37.6313 37.3185 36.9749 37.9749C36.3185 38.6313 35.4283 39 34.5 39H26" stroke="black" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                </svg>
            </div>
        </Paper>
    )
}

CoinCard.propTypes = {
    name: PropTypes.string,
    price: PropTypes.any,
    description: PropTypes.string
};

export default CoinCard;