import React from "react";
import { Paper, styled, Table, TableBody, TableCell, tableCellClasses, TableContainer, TableHead, TablePagination, TableRow } from "@mui/material";
import PropTypes from 'prop-types';
import './QuotationTable.css'


const StyledTableCell = styled(TableCell)(({ theme }) => ({
    [`&.${tableCellClasses.head}`]: {
      backgroundColor: "rgba(0,0,0,0)",
      color: "#828282",
      fontSize: "14px"
    },
    [`&.${tableCellClasses.body}`]: {
      fontSize: 18,
    },
  }));
  
const StyledTableRow = styled(TableRow)(({ theme }) => ({
    // hide last border
    '&:last-child td, &:last-child th': {
        border: 0,
    },
}));

const QuotationTable = (props) => {
    const {
        rows,
        page,
        rowsPerPage,
        count,
        onPageChange,
        onRowsPerPageChange
    } = props;

    const handleChangePage = (event, newPage) => {
        onPageChange(newPage);
    };

    const handleChangeRowsPerPage = (event) => {
        onRowsPerPageChange(parseInt(event.target.value, 10));
        onPageChange(0);
    };

    const formatDate = date => {
        const dateSlice = date.split("-");
        return `${dateSlice[2]}/${dateSlice[1]}/${dateSlice[0]}`;
    }

    const formatVariance = variance => variance.startsWith("-") ? variance : `+${variance}`;

    return (
        <div>
            <TableContainer component={Paper}>
                <Table className="quotation-table-container" aria-label="customized table">
                    <TableHead>
                        <TableRow>
                            <StyledTableCell>Moeda</StyledTableCell>
                            <StyledTableCell align="right">Mínima</StyledTableCell>
                            <StyledTableCell align="right">Máxima</StyledTableCell>
                            <StyledTableCell align="right">Variação</StyledTableCell>
                        </TableRow>
                    </TableHead>
                    <TableBody>
                    {rows.map((row, i) => (
                        <StyledTableRow key={i}>
                        <StyledTableCell component="th" scope="row">
                            <div style={{display: "flex", flexDirection: "row", columnGap: "15px", alignItems: "center"}}>
                                <svg width="64" height="64" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
                                    <rect width="64" height="64" rx="32" fill="#F4C23B"/>
                                    <path d="M32 21V43" stroke="black" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                                    <path d="M37 25H29.5C28.5717 25 27.6815 25.3687 27.0251 26.0251C26.3687 26.6815 26 27.5717 26 28.5C26 29.4283 26.3687 30.3185 27.0251 30.9749C27.6815 31.6313 28.5717 32 29.5 32H34.5C35.4283 32 36.3185 32.3687 36.9749 33.0251C37.6313 33.6815 38 34.5717 38 35.5C38 36.4283 37.6313 37.3185 36.9749 37.9749C36.3185 38.6313 35.4283 39 34.5 39H26" stroke="black" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                                </svg>
                                <div>
                                    <p className="quotation-table-column-name">
                                        {row.name}
                                    </p>
                                    <p className="quotation-table-column-create-date">{formatDate(row.create_date)}</p>
                                </div>
                            </div>
                        </StyledTableCell>
                        <StyledTableCell align="right">{row.min_price}</StyledTableCell>
                        <StyledTableCell align="right">{row.max_price}</StyledTableCell>
                        <StyledTableCell align="right">
                            <div className="quotation-table-column-variance-container"><span className="quotation-table-column-variance-span" style={row.variance.startsWith("-") ? {backgroundColor: "#E0E0E0"} : {} }>{formatVariance(row.variance)}</span></div>
                        </StyledTableCell>
                        </StyledTableRow>
                    ))}
                    </TableBody>
                </Table>
            </TableContainer>
            <TablePagination
                rowsPerPageOptions={[5, 10, 25]}
                component="div"
                count={count}
                rowsPerPage={rowsPerPage}
                page={page}
                onPageChange={handleChangePage}
                onRowsPerPageChange={handleChangeRowsPerPage}
            />
        </div>
    )
}

QuotationTable.propTypes = {
    rows: PropTypes.array,
    page: PropTypes.number,
    rowsPerPage: PropTypes.number,
    count: PropTypes.number,
    onPageChange: PropTypes.func,
    onRowsPerPageChange: PropTypes.func
};

export default QuotationTable;