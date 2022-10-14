import { observable } from 'mobx';
import { Inject, Service } from 'typedi';
import { ViewModel } from '@itcs/react-mvvm';
import { TestService } from '../../service/test/TestService';

@Service('testViewModel')
export class TestViewModel extends ViewModel {
    /** Глобальный объект App */
    app = (window.globalThis as any).App
    /** Признак прав пользователя **/
    @observable isAdmin: boolean = this.app.getMainView().getViewModel().get().isAdmin;

    /** Инициализация ViewModel */
    onInit() {}

    @Inject('testService') testService: TestService;
}