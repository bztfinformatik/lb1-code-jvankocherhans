import React from 'react';
import {
    CDBSidebar,
    CDBSidebarContent,
    CDBSidebarFooter,
    CDBSidebarHeader,
    CDBSidebarMenu,
    CDBSidebarMenuItem,
} from 'cdbreact';

import { NavLink } from 'react-router-dom';

import '../Stylesheets/Navigation.css'

export const Navigation = () => {

    return (
        <>
            <CDBSidebar textColor="#fff" backgroundColor="#111111">
                <CDBSidebarHeader prefix={<i className="fa fa-bars fa-large"></i>}>
                    <a href="/" className="text-decoration-none" style={{ color: 'inherit' }}>
                        Arpa Conda
                    </a>
                </CDBSidebarHeader>

                <CDBSidebarContent className="sidebar-content">
                    <CDBSidebarMenu>
                        <NavLink exact to="/" activeClassName="activeClicked">
                            <CDBSidebarMenuItem icon="columns">Dashboard</CDBSidebarMenuItem>
                        </NavLink>
                        <NavLink exact to="/tables" activeClassName="activeClicked">
                            <CDBSidebarMenuItem icon="table">Show Reactions</CDBSidebarMenuItem>
                        </NavLink>
                        <NavLink exact to="/profile" activeClassName="activeClicked">
                            <CDBSidebarMenuItem icon="table">Show Switches</CDBSidebarMenuItem>
                        </NavLink>
                        <NavLink exact to="/analytics" activeClassName="activeClicked">
                            <CDBSidebarMenuItem icon="chart">Import Client</CDBSidebarMenuItem>
                        </NavLink>
                        <NavLink exact to="/analytics" activeClassName="activeClicked">
                            <CDBSidebarMenuItem icon="chart">Import Script</CDBSidebarMenuItem>
                        </NavLink>
                        <NavLink exact to="/analytics" activeClassName="activeClicked">
                            <CDBSidebarMenuItem icon="chart">Import Switch</CDBSidebarMenuItem>
                        </NavLink>
                        <NavLink exact to="/hero404" target="_blank" activeClassName="activeClicked">
                            <CDBSidebarMenuItem icon="user">Add User</CDBSidebarMenuItem>
                        </NavLink>
                    </CDBSidebarMenu>
                </CDBSidebarContent>

                <CDBSidebarFooter style={{ textAlign: 'center' }}>
                    <div
                        className="sidebar-btn-wrapper"
                        style={{
                            padding: '20px 5px',
                        }}
                    >
                        
                    </div>
                </CDBSidebarFooter>
            </CDBSidebar>
        </>
    )
}