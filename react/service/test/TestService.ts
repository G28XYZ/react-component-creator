import { Inject, Service } from 'typedi';
import { TestApi } from './ApiHelper/TestApi';

@Service('TestService')
export class TestService {
    @Inject('testApi') testApi: TestApi;
}