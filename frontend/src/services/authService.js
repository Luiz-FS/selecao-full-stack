export const login = async (email, password) => {
    const response = await fetch(`${process.env.REACT_APP_AUTH_URL}/api-token-auth/`, {
        method: "POST",
        body: JSON.stringify({
            username: email,
            password: password
        }),
        headers: {
            "Content-Type": "application/json"
        }
    });

    if (response.status !== 200) {
        throw Error("Falha na autenticação");
    }

    const data = await response.json()

    localStorage.setItem("user", JSON.stringify(data));
    return data
}
