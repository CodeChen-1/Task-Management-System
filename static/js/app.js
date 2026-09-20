const BASE_URL = "https://127.0.0.1:8000";
let token = localStorage.getItem("token");
if (token){
    showMainApp()
}

function showLogin(){
    document.getElementById("login-form").style.display = "block";
    document.getElementById("register-form").style.display = "none";
}

function showRegister(){
    document.getElementById("login-form").style.display = "none";
    document.getElementById("register-form").style.display = "block";
}


async function login(){
    const username = document.getElementById("login-username").value;
    const password = document.getElementById("login-password").value;

    try{
        const response = await fetch(`${BASE_URL}/login`,
            {
                method: "POST",
                headers: {"Content-Type": "application/json"},
                body: JSON.stringify({username, password})
            }
        );

    if(response.ok){
        const data = await response.json();
        token = data.access_token; 
        localStorage.setItem("token",token);
        showMainApp();
    }else{
        const error = await response.json();
        alert(error.detail || "Login failed");
    }
    } catch(err){
        alert("Cannot connect to server");
    }
}