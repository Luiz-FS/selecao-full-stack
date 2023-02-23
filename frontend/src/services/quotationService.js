import authHeader from "./authHeader";

export const getQuotations = async (coinId, page, rowsPerPage) => {
    const response = await fetch(`${process.env.REACT_APP_API_URL}/quotation/?coin__id=${coinId}&page=${page}&page_size=${rowsPerPage}`, {
        method: "GET",
        headers: authHeader()
    });

    if (response.status !== 200) {
        throw Error("Falha ao carregar cotações");
    }

    const data = await response.json();
    return data
}
