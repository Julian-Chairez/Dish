"use client";
import React, { useState } from 'react';
import {
  autoSignIn,
  confirmSignUp,
  signUp
} from 'aws-amplify/auth';
import { Amplify } from 'aws-amplify';
import  awsmobile  from '../aws-exports'
Amplify.configure(awsmobile)

const SignUp = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [email, setEmail] = useState('');
  const [phoneNumber, setPhoneNumber] = useState('');

  const handleSignUp = async () => {
    try {
      const { user } = await signUp({
        username,
        password,
        options: {
          userAttributes: {
            email:email,
            phone_number: phoneNumber // E.164 number convention
          },
        }
      });
      console.log('User signed up:', user);
    } catch (error) {
      console.error('Error signing up:', error);
    }
  };

  return (
    <div>
      <input type="text" placeholder="Username" onChange={(e) => setUsername(e.target.value)} />
      <input type="password" placeholder="Password" onChange={(e) => setPassword(e.target.value)} />
      <input type="email" placeholder="Email" onChange={(e) => setEmail(e.target.value)} />
      <input type="phone_number" placeholder="Phone Number" onChange={(e) => setPhoneNumber(e.target.value)} />
      <button onClick={handleSignUp}>Sign Up</button>
    </div>
  );
};

export default SignUp;