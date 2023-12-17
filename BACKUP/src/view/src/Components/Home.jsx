import React from 'react';
import { Navigation } from './Navigation'; 

export const Home = () => {

    return (
        <>
            <div className="App">
                <div style={{ display: 'flex', height: '100vh', overflow: 'scroll initial' }}>
                    <Navigation />

                </div>
            </div>
        </>
    )
}