import React, {useState} from 'react'
import '../style/media.css'
import {NavLink} from 'react-router-dom';
import logo from '../images/logo_atie.svg';
import logo2 from '../images/logo2.svg';
import instagram from "../images/Instagram.png";
import youtube from "../images/Youtube.png";
import whatsapp from "../images/Whatsapp.png";
import telegram from "../images/Telegram.png";

const Header = ({isLight, isDisplay, isBlack}) => {

    const [Light, setIsLight] = useState(false)
    const [display, setDisplay] = useState(false)
    const [showBurger, setShowBurger] = useState(false)
    const [Black, setIsBlack] = useState(false)

    const handleBurger = () => {
        setShowBurger(!showBurger)
    }
    return (
        <header className={`header  ${isLight ? "header__padding" : ""}
         ${isBlack ? "header__cars" : ""} ${isDisplay ? "header__none" : ""}`}>
            <div className="header__main container d-flex justify-between align-center">
                <NavLink to="/" className="header__logo">
                    <img src={logo} alt="" className="logo__img" />
                </NavLink>
                <nav className="header__nav d-flex justify-between">
                    <div className="header__main-link">
                        <NavLink to="/"
                                 className={`header__link ${isLight ? "header__light header__link" : ""}`}>Главная</NavLink>
                    </div>
                    <div className="header__testdrive-link">
                        <NavLink to="/register"
                                 className={`header__link ${isLight ? "header__light" : ""}`}>Регистрация</NavLink>
                    </div>
                    <div className="header__tracking-link">
                        <NavLink to="/login"
                                 className={`header__link ${isLight ? "header__light" : ""}`}>Логин</NavLink>
                    </div>
                    {/*<div className="header__credit-link">*/}
                    {/*    <NavLink to="/credit"*/}
                    {/*             className={`header__link ${isLight ? "header__light" : ""}`}>Кредитование</NavLink>*/}
                    {/*</div>*/}
                    {/*<div className="header__diler-link">*/}
                    {/*    <NavLink to="/diler"*/}
                    {/*             className={`header__link ${isLight ? "header__light" : ""}`}>Дилерам</NavLink>*/}
                    {/*</div>*/}
                    {/*<div className="header__company-link">*/}
                    {/*    <NavLink to="/about" className={`header__link ${isLight ? "header__light" : ""}`}>*/}
                    {/*       O компании</NavLink>*/}
                    {/*</div>div*/}
                </nav>
                {/*<button onClick={handleBurger}*/}
                {/*        className={`header__burger ${showBurger ? "header__burger_active" : ""}${isLight ? "header__nav_light" : ""}`}></button>*/}
                {/*{*/}
                {/*    showBurger && (*/}
                {/*        <nav className="header__nav_burger d-flex flex-column">*/}
                {/*            <NavLink to="/" className="header__nav_logo">*/}
                {/*                <img src={isLight ? logo : ""} alt="" className=""/>*/}
                {/*            </NavLink>*/}
                {/*                <NavLink to="/" className="header__nav_link" onClick={showBurger ? "header__burger_active" : ""}>Главная</NavLink>*/}
                {/*                <NavLink to="/testdrive" className="header__nav_link" onClick={showBurger ? "header__burger_active" : ""}>Тест-драйв</NavLink>*/}
                {/*                <NavLink to="/tracking" className="header__nav_link" onClick={showBurger ? "header__burger_active" : ""}>Трекинг</NavLink>*/}
                {/*                <NavLink to="/credit" className="header__nav_link" onClick={showBurger ? "header__burger_active" : ""}>Кредитование</NavLink>*/}
                {/*                <NavLink to="/diler" className="header__nav_link" onClick={showBurger ? "header__burger_active" : ""}>Дилерам </NavLink>*/}
                {/*                <NavLink to="/about" className="header__nav_link" onClick={showBurger ? "header__burger_active" : ""}>О компании</NavLink>*/}

                {/*            <div className="footer__grid">*/}
                {/*                <a href="" className="header__eclipse"><img src={instagram} alt=""/></a>*/}
                {/*                <a href="https://www.youtube.com/channel/UCQ38-AA8Ec1theWNJEQyz1A/featured"*/}
                {/*                   className="header__eclipse"><img src={youtube} alt=""/></a>*/}
                {/*                <a href="" className="header__eclipse"><img src={whatsapp} alt=""/></a>*/}
                {/*                <a href="" className="header__eclipse"><img src={telegram} alt=""/></a>*/}
                {/*            </div>*/}
                {/*        </nav>*/}
                {/*    )*/}
                {/*}*/}
            </div>
        </header>
    )
}

export default Header