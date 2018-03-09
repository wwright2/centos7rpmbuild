%{!?perl_vendorlib: %define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)}

Name:           perl-Sys-SigAction
Version:        0.23
Release:        1%{?dist}
Summary:        Perl extension for Consistent Signal Handling
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Sys-SigAction/
Source0:        http://www.planet-elektronik.de/CPAN//authors/id/L/LB/LBAXTER/Sys-SigAction-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl >= 0:5.006000
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test::More)
Requires:       perl(POSIX)
Requires:       perl(Test::More)

%description
Prior to version 5.8.0 perl implemented 'unsafe' signal handling. The
reason it is consider unsafe, is that there is a risk that a signal will
arrive, and be handled while perl is changing internal data structures.
This can result in all kinds of subtle and not so subtle problems. For this
reason it has always been recommended that one do as little as possible in
a signal handler, and only variables that already exist be manipulated.

%prep
%setup -q -n Sys-SigAction-%{version}

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
%doc Changes META.json README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Mar 07 2018 Your Name <wwright@nice.com> 0.23-1
- Specfile autogenerated by cpanspec 1.78.