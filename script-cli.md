## STS

Jika aplikasi ingin memberikan akses ke service AWS kepada user yang sudah terautentikasi oleh aplikasi kita, misalkan akses user ke S3 bucket untuk menaruh file pribadi atau menyimpan data pribadi ke DynamoDB. Maka bisa menggunakan token untuk user tersebut, yang ditampikan dialur dibawah.

> User --> Login ke aplikasi --> Aplikasi cek didatabase apakah username dan password benar --> Jika benar, maka aplikasi akan minta token ke STS untuk user tersebut --> STS akan menerima request dan mengecek request --> STS memberikan token ke aplikasi --> Aplikasi mengakses service AWS menggunakan token, misalkan menyimpan profil user ke DynamoDB.

Berikut ini command ke STS
```
aws sts get-federation-token --policy "file://C:\IAM - Allow S3.json" --name fulan
```
Outputnya nanti bisa digunakan oleh aplikasi yang dibangun dengan SDK untuk akses ke service AWS.
```
{
    "Credentials": {
        "AccessKeyId": "XXX",
        "SecretAccessKey": "XXX",
        "SessionToken": "XXX",
        "Expiration": "2021-11-27T19:27:46+00:00"
    },
    "FederatedUser": {
        "FederatedUserId": "890913392175:fulan",
        "Arn": "arn:aws:sts::890913392175:federated-user/fulan"
    },
    "PackedPolicySize": 5
}
```
