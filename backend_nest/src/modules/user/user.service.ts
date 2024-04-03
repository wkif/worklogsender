import { Injectable } from '@nestjs/common';
import { User } from './entity/user.entity';
import { Repository } from 'typeorm';
import { InjectRepository } from '@nestjs/typeorm';

@Injectable()
export class UserService {
  constructor(@InjectRepository(User) private user: Repository<User>) {}
  create({ email, salt, hashPwd, username }) {
    const user = new User();
    user.email = email;
    user.avatar = '';
    user.isactive = true;
    user.passwdSalt = salt;
    user.password = hashPwd;
    user.username = username;
    return this.user.save(user);
  }
  findByemail(email: string) {
    return this.user.findOne({
      where: {
        email,
      },
    });
  }
  async findByName(username: string) {
    const user = await this.user.findOne({
      where: {
        username,
      },
    });
    if (user) {
      return user;
    } else {
      return void 0;
    }
  }
}
