export enum Role{
    User = 'User',
    Admin = 'Admin'
}

export interface User{
    id: number;
    firstname: string;
    lastname: string;
    username: string;
    password: string;
    role: Role;
    jwtToken?: string;
}