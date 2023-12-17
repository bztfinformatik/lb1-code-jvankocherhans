import React, { useState } from 'react';
import { MDBContainer, MDBInput, MDBBtn } from 'mdb-react-ui-kit';

export const Login = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [loginError, setLoginError] = useState('');

    const handleLogin = async () => {
        try {
            const response = await fetch('http://localhost', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ username, password }),
            });

            if (response.ok) {
                setLoginError('Login erfolgreich');
            } else {
                const errorText = await response.text(); 
                setLoginError(`Login fehlgeschlagen: ${errorText}`);
            }
        } catch (error) {
            console.error('Fehler beim Login:', error);
            setLoginError(`Fehler beim Login: ${error.message}`);
        }
    };

    return (
        <MDBContainer className="p-3 my-5 d-flex flex-column w-50">
            <MDBInput
                wrapperClass='mb-4'
                label='Username'
                id='form1'
                type='email'
                value={username}
                onChange={(e) => setUsername(e.target.value)}
            />
            <MDBInput
                wrapperClass='mb-4'
                label='Password'
                id='form2'
                type='password'
                value={password}
                onChange={(e) => setPassword(e.target.value)}
            />

            <MDBBtn className="mb-4" onClick={handleLogin}>
                Log in
            </MDBBtn>

            <div className="text-center">
                {loginError}
            </div>
        </MDBContainer>
    );
};
