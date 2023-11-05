import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from "@angular/forms";
import { first } from 'rxjs/operators';
import { AuthenticationService } from 'src/app/services/authentication.service';
import { Router, ActivatedRoute } from '@angular/router';


@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  
  // loading = true;
  // error = '';

  constructor(private formBuilder: FormBuilder, private authService: AuthenticationService, 
    private router: Router, private rout: ActivatedRoute){
  }

  loginForm! : FormGroup;

  ngOnInit(): void {
    this.loginForm = this.formBuilder.group(
      {
        username: ['', Validators.required],
        password: ['', Validators.required]
      }
    );
  }


  get f(){
    return this.loginForm.controls;
  }
  
  onSubmit = () => {
    if(this.loginForm.invalid){
      return;
    }

    this.authService.login(this.f['username'].value, this.f['password'].value)
    .pipe(first())
    .subscribe({

      next: () => {
          const returnUrl = '/';
          this.router.navigateByUrl(returnUrl);
      },
      error: error => {
        console.log("not access");
        // this.loading = false;
        // this.error = error;
      }
    });
    
  }
}