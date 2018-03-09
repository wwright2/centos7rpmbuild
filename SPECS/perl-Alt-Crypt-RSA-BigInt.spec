%{!?perl_vendorlib: %define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)}

Name:           perl-Alt-Crypt-RSA-BigInt
Version:        0.06
Release:        1%{?dist}
Summary:        RSA public-key cryptosystem, using Math::BigInt
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Alt-Crypt-RSA-BigInt/
Source0:        http://www.cpan.org/authors/id/D/DA/DANAJ/Alt-Crypt-RSA-BigInt-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl >= 0:5.008
BuildRequires:  perl(Benchmark)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Loader)
BuildRequires:  perl(Convert::ASCII::Armour)
BuildRequires:  perl(Crypt::Blowfish)
BuildRequires:  perl(Crypt::CBC) >= 2.17
BuildRequires:  perl(Data::Buffer)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Digest::MD2)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Math::BigInt) >= 1.78
BuildRequires:  perl(Math::BigInt::GMP)
BuildRequires:  perl(Math::Prime::Util) >= 0.64
BuildRequires:  perl(Math::Prime::Util::GMP)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Sort::Versions)
BuildRequires:  perl(Test::More) >= 0.45
BuildRequires:  perl(Tie::EncryptedHash)
Requires:       perl(Carp)
Requires:       perl(Class::Loader)
Requires:       perl(Convert::ASCII::Armour)
Requires:       perl(Crypt::Blowfish)
Requires:       perl(Crypt::CBC) >= 2.17
Requires:       perl(Data::Buffer)
Requires:       perl(Data::Dumper)
Requires:       perl(Digest::MD2)
Requires:       perl(Digest::MD5)
Requires:       perl(Digest::SHA)
Requires:       perl(Exporter)
Requires:       perl(Math::BigInt) >= 1.78
Requires:       perl(Math::BigInt::GMP)
Requires:       perl(Math::Prime::Util) >= 0.64
Requires:       perl(Math::Prime::Util::GMP)
Requires:       perl(Sort::Versions)
Requires:       perl(Tie::EncryptedHash)

%description
This is a modification of the Crypt::RSA module to remove all use and
dependencies on Pari and Math::Pari.

%prep
%setup -q -n Alt-Crypt-RSA-BigInt-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check || :
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes Changes.old LICENSE META.json README TODO
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Mar 07 2018 Your Name <wwright@nice.com> 0.06-1
- Specfile autogenerated by cpanspec 1.78.
