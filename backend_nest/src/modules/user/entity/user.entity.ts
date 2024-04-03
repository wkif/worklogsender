import { Column, Entity, PrimaryGeneratedColumn } from 'typeorm';

@Entity()
export class User {
  @PrimaryGeneratedColumn()
  id: number;
  @Column()
  email: string;
  @Column()
  username: string;
  @Column()
  avatar: string;
  @Column()
  password: string;
  @Column()
  passwdSalt: string;
  @Column()
  isactive: boolean;
}
