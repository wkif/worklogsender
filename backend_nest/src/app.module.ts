import { Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';
import { ConfigModule } from '@nestjs/config';

import { AppController } from './app.controller';
import { AppService } from './app.service';
import { UserModule } from './modules/user/user.module';
import { AuthModule } from './modules/auth/auth.module';

import { jwtAuthGuard } from './modules/auth/jwt-auth.grard';

import config from './common/config';
import { APP_GUARD } from '@nestjs/core';
@Module({
  imports: [
    ConfigModule.forRoot({
      isGlobal: true,
      load: [config],
    }),
    TypeOrmModule.forRoot({
      type: 'mysql',
      port: process.env.MYSQL_PORT as unknown as number,
      username: process.env.MYSQL_USERNAME,
      host: process.env.MYSQL_HOST,
      password: process.env.MYSQL_PASSWORD,
      database: process.env.MYSQL_DATABASE,
      synchronize: true,
      autoLoadEntities: true,
    }),
    UserModule,
    AuthModule,
  ],
  controllers: [AppController],
  providers: [
    AppService,
    {
      provide: APP_GUARD,
      useClass: jwtAuthGuard,
    },
  ],
})
export class AppModule {}
