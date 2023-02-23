import authHeader from "./authHeader";

export const getCoins = async () => {
    const response = await fetch(`${process.env.REACT_APP_API_URL}/coin/`, {
        method: "GET",
        headers: authHeader()
    });

    if (response.status !== 200) {
        throw Error("Falha ao carregar moedas");
    }

    const data = await response.json();
    return data["results"]
}
