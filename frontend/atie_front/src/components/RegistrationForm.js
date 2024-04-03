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
              <input type="email" name="email" placeholder="Email" value={formData.email} onChange={handleInputChange}/>
              <input type="password" name="password" placeholder="Пароль" value={formData.password}
                     onChange={handleInputChange}/>
              <input type="password" name="password2" placeholder="Подтвердите пароль" value={formData.password2}
                     onChange={handleInputChange}/>
              <input type="text" name="first_name" placeholder="Имя" value={formData.first_name}
                     onChange={handleInputChange}/>
              <input type="text" name="last_name" placeholder="Фамилия" value={formData.last_name}
                     onChange={handleInputChange}/>
              <button type="submit">Зарегистрироваться</button>
          </form>
  );
};
export default RegistrationForm;