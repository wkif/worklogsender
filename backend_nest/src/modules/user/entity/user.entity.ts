import { Column, Entity, OneToMany, PrimaryGeneratedColumn } from 'typeorm';

import { Link } from 'src/modules/links/entity/link.entity';

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
  @OneToMany(() => Link, (link) => link.user)
  links: Link[];
}
