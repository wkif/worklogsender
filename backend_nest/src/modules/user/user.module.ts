import { Module } from '@nestjs/common';
import { UserController } from './user.controller';
import { UserService } from './user.service';
import { TypeOrmModule } from '@nestjs/typeorm';
import { User } from './entity/user.entity';
import { AuthService } from '../auth/auth.service';
import { JwtModule } from '@nestjs/jwt';
import { Link } from '../links/entity/link.entity';
@Module({
  imports: [TypeOrmModule.forFeature([User, Link]), JwtModule],
  controllers: [UserController],
  providers: [UserService, AuthService],
  exports: [UserService],
})
export class UserModule {}
