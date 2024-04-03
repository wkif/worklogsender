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
  async Login(@Body() data: { email: string; password: string }) {
    // const authResult = await this.authservice.validateUser(
    //   data.email,
    //   data.password,
    // );
    return {
      data,
    };
  }
}
