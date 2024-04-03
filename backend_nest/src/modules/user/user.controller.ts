import { Body, Controller, Post, HttpCode } from '@nestjs/common';
import { Result } from 'src/common/result.interface';
// import { AuthGuard } from '@nestjs/passport';

// 引入加密函数
import { makeSalt, encryptPassword } from '../../utils/cryptogram';

import { UserService } from './user.service';

@Controller('user')
export class UserController {
  constructor(private readonly userService: UserService) {}
  @Post('register')
  @HttpCode(200)
  async register(
    @Body() data: { username: string; password: string; email: string },
  ): Promise<Result> {
    if (!data.username || !data.password || !data.email) {
      return {
        code: 500,
        msg: '请完整填写信息',
        data: {},
      };
    }
    const findByemail = await this.userService.findByemail(data.email);
    if (findByemail) {
      return {
        code: 500,
        msg: '邮箱已注册',
        data: {},
      };
    }
    const findByName = await this.userService.findByName(data.username);
    if (findByName) {
      return {
        code: 500,
        msg: '用户名已注册',
        data: {},
      };
    }
    const salt = makeSalt();
    const hashPwd = encryptPassword(data.password, salt);

    try {
      const res = await this.userService.create({
        email: data.email,
        salt: salt,
        hashPwd: hashPwd,
        username: data.username,
      });
      if (res) {
        return {
          code: 200,
          msg: '注册成功',
          data: {},
        };
      }
    } catch (error) {
      return {
        code: 500,
        msg: error,
        data: {},
      };
    }
  }

  @Post('login')
  async Login(
    @Body() data: { email: string; password: string },
  ): Promise<Result> {
    // const authResult = await this.authservice.validateUser(
    //   data.email,
    //   data.password,
    // );
    const user = await this.userService.findByemail(data.email);

    if (user) {
      const hashedPassword = user.password;
      const salt = user.passwdSalt;
      // 通过密码盐，加密传参，再与数据库里的比较，判断是否相等
      const hashPassword = encryptPassword(data.password, salt);
      if (hashedPassword === hashPassword) {
        // 密码正确
        return {
          code: 1,
          user,
        };
      } else {
        // 密码错误
        return {
          code: 400,
          msg: '密码错误',
          data: {},
        };
      }
    }
    // 查无此人
    return {
      code: 3,
      user: null,
    };
    // return {
    //   data,
    // };
  }
}
