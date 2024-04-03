import React, {useState} from 'react';
import {BrowserRouter as Router, Route, Routes, Link} from 'react-router-dom';
import Login from './components/Login';
import RegistrationForm from './components/RegistrationForm';
import Header from "./components/Header";
import './style/App.css';

const App = () => {

    const [isLight, setIsLight] = useState(false)
    const [isDisplay, setDisplay] = useState(false)
    const [isBlack, setIsBlack] = useState(false)

    const handleLogin = (userData) => {
        console.log('Выполняется вход:', userData);
        // Здесь можно выполнить дополнительные действия при входе, например, обновить состояние авторизации
    };

    const handleRegistration = (userData) => {
        console.log('Выполняется регистрация:', userData);
        // Здесь можно выполнить дополнительные действия при регистрации, например, перенаправление на другую страницу
    };

    return (
        <Router>
            <Header isLight={isLight} isDisplay={isDisplay} isBlack={isBlack}/>
            <Routes>
                {/*<Route path="/" element={<Home />} />*/}
                <Route path="/login" element={<Login onLogin={handleLogin}/>}/>
                <Route path="/register" element={<RegistrationForm onRegistration={handleRegistration}/>}/>

            </Routes>

        </Router>
    );
};

export default App;
