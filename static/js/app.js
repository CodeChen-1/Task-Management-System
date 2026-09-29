const BASE_URL = "http://127.0.0.1:8000";
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

async function register() {
    const username = document.getElementById("reg-username").value;
    const email = document.getElementById("reg-email").value;
    const password = document.getElementById("reg-password").value;

    try{
        const response = await fetch(`${BASE_URL}/register`, {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({username, email ,password})
        });
        if (response.ok){
            alert("Regisatration successful! Please login.")
            showLogin();
        }else{
            const error = await response.json();
            alert(error.detail || "Registratiob failed");
        }
    }catch(err){
        alert("Cannot connect to server")
    }
}

function logout() {
    token = null;
    localStorage.removeItem("token");
    document.getElementById("auth-form").style.display = "block";
    document.getElementById("main-app").style.display = "none";
}

function showMainApp() {
    document.getElementById("auth-form").style.display = "none";
    document.getElementById("main-app").style.display = "block";
    loadTasks();
}