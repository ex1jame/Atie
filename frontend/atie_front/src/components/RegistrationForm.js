import React, { useState } from 'react'

import axios from "axios";
const RegistrationForm = ({ onRegistrationSuccess }) => {
  const [formData, setFormData] = useState({

    email: '',
    password: '',
    password2: '',
    first_name: '',
    last_name: '',

  });

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:8000/api/v1/accounts/register/', formData);
      onRegistrationSuccess(response.data);
    } catch (error) {
      console.error('Ошибка регистрации:', error);
    }
  };

  return (
      <form onSubmit={handleSubmit}>
          <section className="login__hero">
              <div className="login__block d-flex align-center justify-center flex-column">
                  {/*<img src={} alt="" className="login__img"/>*/}
                  <p className="login__desc">Registration</p>
                  <div className="login__form d-flex flex-column">
                      <input type="email" name="email" placeholder="Email" value={formData.email}
                             onChange={handleInputChange}/>
                      <input type="password" name="password" placeholder="Пароль" value={formData.password}
                             onChange={handleInputChange}/>
                      <input type="password" name="password2" placeholder="Подтвердите пароль"
                             value={formData.password2}
                             onChange={handleInputChange}/>
                      <input type="text" name="first_name" placeholder="Имя" value={formData.first_name}
                             onChange={handleInputChange}/>
                      <input type="text" name="last_name" placeholder="Фамилия" value={formData.last_name}
                             onChange={handleInputChange}/>
                      <div className="login__d-flex justify-between">
                          <a href="#" className="login__password">Remember me</a>
                          <a href="#" className="login__password">Forgot your password?</a>
                      </div>
                  </div>
                  <button type="submit" className="orange_btn">Зарегистрироваться</button>
              </div>
          </section>



      </form>
  );
};
export default RegistrationForm;