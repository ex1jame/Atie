import React, { useState } from 'react';
import axios from 'axios';
import '../style/login.css'

const Login = ({ onLogin }) => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleLogin = async (e) => {
    e.preventDefault(); // Предотвращение действия по умолчанию
    try {
      // Отправка POST запроса для входа пользователя
      const response = await axios.post('http://localhost:8000/api/v1/accounts/login/', { email, password });
      const token = response.data.access; // Получение токена из ответа
      localStorage.setItem('token', token); // Сохранение токена в localStorage
      onLogin(token); // Вызов функции onLogin с передачей токена
    } catch (error) {
      console.error('Ошибка входа:', error); // Обработка ошибок входа
    }
  };

  return (
      <form onSubmit={handleLogin}>
        <section className="login__hero">
          <div className="login__block d-flex align-center justify-center flex-column">
            {/*<img src={} alt="" className="login__img"/>*/}
            <p className="login__desc">Login</p>
            <div className="login__form d-flex flex-column">
              <input type="email" placeholder="Email" value={email} onChange={(e) => setEmail(e.target.value)}/>
              <input type="password" placeholder="Пароль" value={password}
                     onChange={(e) => setPassword(e.target.value)}/>

              <div className="login__d-flex justify-between">
                <a href="#" className="login__password">Remember me</a>
                <a href="#" className="login__password">Forgot your password?</a>
              </div>
            </div>


            <button type="submit" className="orange_btn">Login</button>


          </div>
        </section>
      </form>
  );
};

export default Login;
